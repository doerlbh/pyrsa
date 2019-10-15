#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of RSA Dataset classes for arbitrary user-defined data
@author: baihan
"""
import pyrsa as rsa
from pyrsa.data.dataset import DatasetBase
import numpy as np

def preprocess_example(rawdata=None):
    raise NotImplementedError(
            "preprocess_fmri function not implemented!")

class DatasetExample(DatasetBase): 
    """
    DatasetExample class is a variant of Dataset that takes in any arbitrary user defined data and process it into standard Dataset format.
    """
    def __init__(self, rawdata=None,preprocess=preprocess_example):
        measurements,descriptors,obs_descriptors,channel_descriptors=preprocess(rawdata)

        def split_obs(self, by=descriptor):
        """ Returns a list Datasets splited by obs
        Args:
            descriptor(String): the descriptor by which the splitting is made

        Returns:
            list of Datasets, splitted by the selected obs_descriptor
        """
        # TODO
        

    def split_channel(self, by=descriptor):
        """ Returns a list Datasets splited by channels
        Args:
            descriptor(String): the descriptor by which the splitting is made

        Returns:
            list of Datasets,  splitted by the selected channel_descriptor
        """
        # TODO

    def subset_obs(self, by=value):
        """ Returns a subsetted Dataset defined by certain obs
        Args:
            value(HashMap<String,Float or String>): the value by which the subset selection is made from obs dimension

        Returns:
            Dataset, with subset defined by the selected obs_descriptor
        """
        # TODO

    def subset_channel(self, by=value):
        """ Returns a subsetted Dataset defined by certain channel
        Args:
            value(HashMap<String,Float or String>): the value by which the subset selection is made from channel dimension

        Returns:
            Dataset, with subset defined by the selected channel_descriptor
        """
        # TODO