# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Template file used by ExpGenerator to generate the actual
permutations.py file by replacing $XXXXXXXX tokens with desired values.

This permutations.py file was generated by:
'~/nta/eng/lib/python2.6/site-packages/nupic/frameworks/opf/expGenerator/ExpGenerator.py'
"""


from nupic.swarming.permutationhelpers import *

# The name of the field being predicted.  Any allowed permutation MUST contain
# the prediction field.
# (generated from PREDICTION_FIELD)
predictedField = 'consumption'

permutations = {
  
  'modelParams': {
    'inferenceType': PermuteChoices(['NontemporalMultiStep', 'TemporalMultiStep']),
  
    'sensorParams': {
      'encoders': {
        'timestamp_dayOfWeek': PermuteEncoder(fieldName='timestamp', encoderClass='DateEncoder.dayOfWeek', radius=PermuteFloat(1.000000, 6.000000), w=21),
        'timestamp_timeOfDay': PermuteEncoder(fieldName='timestamp', encoderClass='DateEncoder.timeOfDay', radius=PermuteFloat(0.500000, 12.000000), w=21),
        'consumption': PermuteEncoder(fieldName='consumption', encoderClass='AdaptiveScalarEncoder', n=PermuteInt(28, 521), w=21, clipInput=True),
        'timestamp_weekend': PermuteEncoder(fieldName='timestamp', encoderClass='DateEncoder.weekend', radius=PermuteChoices([1]), w=21),
      },
    },
  
  
    'tpParams': {
      'minThreshold': PermuteInt(9, 12),
      'activationThreshold': PermuteInt(12, 16),
      'pamLength': PermuteInt(1, 5),
    },
  
  
    }
}


# Fields selected for final swarm report;
# NOTE: These values are used as regular expressions by RunPermutations.py's
#       report generator
# (fieldname values generated from PERM_PREDICTED_FIELD_NAME)
report = [
          '.*consumption.*',
         ]

# Permutation optimization setting: either minimize or maximize metric
# used by RunPermutations.
# NOTE: The value is used as a regular expressions by RunPermutations.py's
#       report generator
# (generated from minimize = 'prediction:aae:window=1000:field=consumption')
minimize = "multiStepBestPredictions:multiStep:errorMetric='aae':steps=1:window=1000:field=consumption"



#############################################################################
def permutationFilter(perm):
  """ This function can be used to selectively filter out specific permutation
  combinations. It is called by RunPermutations for every possible permutation
  of the variables in the permutations dict. It should return True for valid a
  combination of permutation values and False for an invalid one. 
  
  Parameters:
  ---------------------------------------------------------
  perm: dict of one possible combination of name:value
        pairs chosen from permutations.
  """
  
  # An example of how to use this
  #if perm['__consumption_encoder']['maxval'] > 300:
  #  return False;
  # 
  return True
