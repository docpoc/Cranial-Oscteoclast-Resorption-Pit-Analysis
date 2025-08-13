"""


:author: Pat O'Connor
:contact: 
:email: oconnojp@njms.rutgers.edu
:organization: Rutgers-New Jersey Medical School
:address: Newark, NJ
:copyright: 
:date: Nov 20 2024 14:17
:dragonflyVersion: 2024.1.0.1613
:UUID: 003f3853a77411ef960c46fa662930df
"""

__version__ = '1.0.2'

"""


:author: Pat O'Connor
:contact: 
:email: oconnojp@njms.rutgers.edu
:organization: Rutgers-New Jersey Medical School
:address: Newark, NJ
:copyright: 
:date: Nov 20 2024 14:16
:dragonflyVersion: 2024.1.0.1613
:UUID: 003f3853a77411ef960c46fa662930df
"""

# Action log Wed Nov 20 14:17:08 2024

# Macro name: Make multiROI to ROI

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
# aProgress = orsObj('13C940926E844E418AEB9CE0AF47DDA9CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: startWorkingProgressWithID
:execution: execute

:param aProgress: 
:type aProgress: ORSModel.ors.Progress
:param iID: 
:type iID: int
:param bCancellable: 
:type bCancellable: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
iID = 45

bCancellable = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aProgress.startWorkingProgressWithID(iID=iID,
                                     bCancellable=bCancellable,
                                     logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new ROI by taking all the voxels from all the labels of the MultiROI

:name: createROIFromLabeledROI
:execution: execute

:param aMultiROI: a MultiROI
:type aMultiROI: ORSModel.ors.MultiROI
:const aMultiROI: True
:param aProgress: progress object
:type aProgress: ORSModel.ors.Progress

:return aROI: a ROI
:rtype aROI: ORSModel.ors.ROI
"""

# Interface method
aROI = OrsVolumeROITools.createROIFromLabeledROI(aMultiROI=aMultiROI,
                                                 IProgress=aProgress)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aROI = orsObj('B76537A08CF0411A849FC33F70551C29CxvVolume_ROI')

# ----- END RETURNED VALUES DEFINITION ----- #
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
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param aROI: 
:type aROI: ORSModel.ors.Managed
"""

# Interface method
aROI.publish(logging=True)

# ********** END MACRO ********** #

