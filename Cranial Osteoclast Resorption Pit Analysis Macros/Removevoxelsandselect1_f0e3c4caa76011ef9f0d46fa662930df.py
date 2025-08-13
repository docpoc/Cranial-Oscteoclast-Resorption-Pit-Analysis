"""


:author: Pat O'Connor
:contact: 
:email: oconnojp@njms.rutgers.edu
:organization: Rutgers-New Jersey Medical School
:address: Newark, NJ
:copyright: 
:date: Nov 20 2024 11:59
:dragonflyVersion: 2024.1.0.1613
:UUID: f0e3c4caa76011ef9f0d46fa662930df
"""

__version__ = '1.0.2'

# Action log Wed Nov 20 12:00:27 2024

# Macro name: Remove voxels and select1

# ********** BEGIN MACRO ********** #
"""
Sets the currently active global state

:name: setCurrentGlobalState
:execution: execute

:param instance: context instance
:type instance: plugin instance
:param state: new state
:type state: str

:return globalStateChangeIsSuccessful: indicates if the change was successful
:rtype globalStateChangeIsSuccessful: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
instance = None

state = 'OrsStateTrack'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
globalStateChangeIsSuccessful = WorkingContext.setCurrentGlobalState(instance=instance,
                                                                     state=state)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# globalStateChangeIsSuccessful = True

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress: the created instance of class Progress
:rtype aProgress: ORSModel.ors.Progress
"""

# Interface method
aProgress = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress = orsObj('A3C63C208DA34EDEA403C49E91CBEBF7CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Removes small or big objects of a ROI based on their voxel count.

:name: processIslands
:execution: execute

:param aROI: the ROI to modify
:type aROI: ORSModel.ors.ROI
:param voxelCountThreshold: voxel count threshold
:type voxelCountThreshold: int
:param keepLargeObjects: if True, only the objects having a voxel count greater than or equal to
    the count threshold will be kept; if False, only the objects having a voxel count smaller than or equal to
    the count threshold will be kept.
:type keepLargeObjects: bool
:param as26Connected: if True, the connectivity will be made using 26 neighbors; if False, the connectivity
    will be made using 6 neighbors.
:type as26Connected: bool
:param aProgress: progress object
:type aProgress: ORSModel.ors.Progress
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
voxelCountThreshold = 75

keepLargeObjects = True

as26Connected = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
OrsProcessIslands_9ea2ae92d95911e89b0d448a5b5d70c0.processIslands(aROI=aROI,
                                                                  voxelCountThreshold=voxelCountThreshold,
                                                                  keepLargeObjects=keepLargeObjects,
                                                                  as26Connected=as26Connected,
                                                                  aProgress=aProgress)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress: 
:type aProgress: ORSModel.ors.Managed
"""

# Interface method
aProgress.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param aROI: 
:type aROI: ORSModel.ors.Managed
:param newVal: 
:type newVal: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal = 'Voxels Removed'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aROI.setTitle(newVal=newVal,
              logging=True)

# ********** END MACRO ********** #

