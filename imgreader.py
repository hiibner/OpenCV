import cv2
import os
from sift_object import SiftObject
from skeletonizer import skeletonize
from resizer import resize
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html


def choose_lower_value(x, y):
    if x > y:
        return y
    else:
        return x


def invertiere(x):
    return 1/x if x > 1 else x


def find_files(directory):
    global filenames
    for filname in os.walk(directory):
        filenames = filname[2]
        break
    return filenames

# img = cv2.drawKeypoints(img,keypoints,None)

# ORB Detector
# orb = cv2.ORB_create()
# kp1, desc1 = orb.detectAndCompute(img1, None)
# kp2, desc2 = orb.detectAndCompute(img2, None)

# BruteForce SIFT
# Brute Force Matching ERKLAERBEDARF WIESO NORMHAMMING / CROSSCHEC nur das beste matchin von der anderen descriptr menge


def start_matching(img1, img2, kp1, kp2, desc1, desc2, knn=True):
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

# fuer flann
# index_params = dict(algorithm = 0, trees = 5)
# search_params = dict()
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(desc1,desc2,k=2)
# good_points = []
# for m, n in matches:
#     if m.distance < 0.6*n.distance:
#         good_points.append(m)

# result = cv2.drawMatches(img1,kp1 ,img2, kp2, matching_result[:10], None, flags=2)


def analyzer(input_file_data, input_file_name, knn, skel, res, database_directory, gui, pickle_path):
    global databaseobjects
    databaseobjects = []
    directory = database_directory   #"C:/Users/Hyu/PycharmProjects/OpenCV/monograms"

    img1 = input_file_data


    sift = cv2.xfeatures2d.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(img1, None)
    input_sift_object = SiftObject(input_file_name, input_file_data, kp1, desc1)

    #Skelettierung
    input_sift_object.img_data_skeleton = skeletonize(img1)
    kp_input_skel, desc_input_skel = sift.detectAndCompute(input_sift_object.img_data_skeleton, None)
    input_sift_object.keypoint_skeleton = kp_input_skel
    input_sift_object.descriptor_skeleton = desc_input_skel


    if pickle_path == None:

        files = find_files(directory)


        #Iteriere über Gesamten Monogramm Ordner
        countersteps = 100 / len(files)
        counter = 0
        for i in files:
            databaseimg = cv2.imread(database_directory+ "/" + str(i), cv2.IMREAD_GRAYSCALE)


            kp, desc = sift.detectAndCompute(databaseimg, None)

            # Um Matching fehler beim Skeletonizen zu entfernen
            if kp == [] and desc == None:
                continue

            # Um matching fehler beim Skeletonizen zu entfernen
            if len(kp) == 1:
                continue

            monogram = SiftObject(i, databaseimg, kp, desc)

            #Skelett bilden
            monogram.img_data_skeleton = skeletonize(databaseimg)
            kp_skel, desc_skel = sift.detectAndCompute(monogram.img_data_skeleton, None)
            monogram.keypoint_skeleton = kp_skel
            monogram.descriptor_skeleton = desc_skel

            # Um Matching fehler beim Skeletonizen zu entfernen
            if kp_skel == [] and desc_skel == None:
                continue

            # Um matching fehler beim Skeletonizen zu entfernen
            if len(kp_skel) == 1:
                continue

            databaseobjects.append(monogram)


            counter = counter + countersteps
            gui.progressBar.setValue(counter)


        # Serialisierung
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

    databaseobjects = sorted(databaseobjects, key=lambda x: x.precision, reverse=True)

    return input_sift_object, databaseobjects
