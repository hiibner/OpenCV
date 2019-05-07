#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Huy Luong
# Created Date: 07.05.2019
# License: GNU GPL
# Inspired: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html
# =============================================================================
# Imports
import cv2
import os
from sift_object import SiftObject
from skeletonizer import skeletonize
from resizer import resize
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
# =============================================================================

def invertiere(x):
    """

    :param x: ratio bigger or smaller than 1
    :return: ratio smaller than 1
    """
    return 1/x if x > 1 else x


def find_files(directory):
    """

    :param directory: directory to traverse
    :return: list of all files
    """
    global filenames
    for filname in os.walk(directory):
        filenames = filname[2]
        break
    return filenames


def start_matching(img1, img2, kp1, kp2, desc1, desc2, knn=True):
    """
    matching the keypoints of 2 images
    :param img1: imgdata of inputimage
    :param img2: imgdata of databaseimages
    :param kp1: keypoints of inputimage
    :param kp2: keypoints of databaseimages
    :param desc1: descriptors of inputimage
    :param desc2: descriptors of databaseimage
    :param knn: Bool--> activate ratiotest
    :return: matching_result: matchingimage of to keypoints; matches/good_matches: list of matched Keypoints
    """
    if knn:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
        matches = bf.knnMatch(desc1, desc2, k=2)
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75*n.distance:
                good_matches.append([m])

        matching_result = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=2)
        return matching_result, good_matches

    else:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = bf.match(desc1, desc2)
        matches = sorted(matches, key=lambda x: x.distance)
        matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)
        return matching_result, matches



def analyzer(input_file_data, input_file_name, knn, skel, database_directory, gui, pickle_path):
    """

    :param input_file_data: pixeldata of inputimage
    :param input_file_name: filename of the inputimage
    :param knn: Bool: activation of Ratio Test
    :param skel: Bool: activation of Skeletonizer
    :param database_directory: directory of the monogramms
    :param gui: parameter of the gui
    :param pickle_path: path of the picklefile
    :return: input_sift_object: inputimage as SIFTObject; databaseobjects[]: ordered list of matched monogramms
    """
    global databaseobjects
    databaseobjects = []
    directory = database_directory

    img1 = input_file_data


    sift = cv2.xfeatures2d.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(img1, None)
    input_sift_object = SiftObject(input_file_name, input_file_data, kp1, desc1)

    #Skelettonizing the inputimage
    input_sift_object.img_data_skeleton = skeletonize(img1)
    kp_input_skel, desc_input_skel = sift.detectAndCompute(input_sift_object.img_data_skeleton, None)
    input_sift_object.keypoint_skeleton = kp_input_skel
    input_sift_object.descriptor_skeleton = desc_input_skel


    if pickle_path == None:
        #Create Keypoints and Descriptors of Images
        files = find_files(directory)


        #Progessbar of the GUI
        countersteps = 100 / len(files)
        counter = 0
        # Iterate over monogrammfolder
        for i in files:
            databaseimg = cv2.imread(database_directory+ "/" + str(i), cv2.IMREAD_GRAYSCALE)


            kp, desc = sift.detectAndCompute(databaseimg, None)

            # remove images without keypoints
            if kp == [] and desc == None:
                continue

            # remove images with less than 2 keypoints
            if len(kp) == 1:
                continue

            monogram = SiftObject(i, databaseimg, kp, desc)

            #Skelettonize monogramms of the folder
            monogram.img_data_skeleton = skeletonize(databaseimg)
            kp_skel, desc_skel = sift.detectAndCompute(monogram.img_data_skeleton, None)
            monogram.keypoint_skeleton = kp_skel
            monogram.descriptor_skeleton = desc_skel

            # remove images without keypoints
            if kp_skel == [] and desc_skel == None:
                continue

            # remove images with less than 2 keypoints
            if len(kp_skel) == 1:
                continue

            databaseobjects.append(monogram)


            counter = counter + countersteps
            gui.progressBar.setValue(counter)


        # Serialisation
        for item in databaseobjects:
            item.encodeKeypointsToPickle()
        pickle_out = open("dict.pickle", "wb")
        pickle.dump(databaseobjects, pickle_out)
        pickle_out.close()
        pickle_in = open("dict.pickle", "rb")
        loaded_data = pickle.load(pickle_in)
        for item in loaded_data:
            item.decodePickleToKeypoints()
        databaseobjects = loaded_data
    else:
        pickle_in = open(pickle_path, "rb")
        loaded_data = pickle.load(pickle_in)
        for item in loaded_data:
            item.decodePickleToKeypoints()
        databaseobjects = loaded_data

    #Matching of each image of the monogramm folder with the input image
    for i in databaseobjects:
        database_image = i.imgdata
        kp_database_image = i.keypoint
        desc_database_image = i.descriptor

        input_image = input_sift_object.imgdata
        kp_input_image = input_sift_object.keypoint
        desc_input_image = input_sift_object.descriptor

        if skel :
            database_image = i.img_data_skeleton
            kp_database_image = i.keypoint_skeleton
            desc_database_image = i.descriptor_skeleton

            input_image = input_sift_object.img_data_skeleton
            kp_input_image = input_sift_object.keypoint_skeleton
            desc_input_image = input_sift_object.descriptor_skeleton


        matching_result, matches = start_matching(input_image, database_image, kp_input_image, kp_database_image, desc_input_image, desc_database_image, knn)
        ratio = len(kp_input_image) / len(kp_database_image)
        ratio = invertiere(ratio)
        i.precision = 0 if len(kp_input_image)==0 or len(kp_database_image)==0 else (len(matches) / len(kp_input_image))*ratio
        i.ratio = ratio
        i.matching_result = matching_result
        i.matches = matches

    #List of all monogramms matched with the inputimage
    databaseobjects = sorted(databaseobjects, key=lambda x: x.precision, reverse=True)

    return input_sift_object, databaseobjects
