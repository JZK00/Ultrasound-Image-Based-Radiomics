import SimpleITK as sitk
from radiomics import featureextractor

# Instantiate extractor with parameter file
extractor = featureextractor.RadiomicsFeatureExtractor(r'E:/Experiments/Likun-Wang/datas/ul.yaml')

# Set path to mask
ma_path = 'E:/Experiments/Likun-Wang/datas/1.nrrd'
label = 1  # Change this if the ROI in your mask is identified by a different value

# Load the image and extract a color channel
color_channel = 0
im = sitk.ReadImage(r'E:/Experiments/Likun-Wang/datas/1.dcm')
selector = sitk.VectorIndexSelectionCastImageFilter()
selector.SetIndex(color_channel)
im = selector.Execute(im)

# Run the extractor
results = extractor.execute(im, ma_path, label=label)
print(results)