# StellarDataset_ML

This is the ML group project for Misk Data Science Immersive Course, the aim for this project is to develop the best machine learning model to classify stars based on their spectral characteristics.

## This Repo includes:

- Introduction.
- Exploratory Data Analysis (EDA).
- K-nearest Neighbors Algorithm.
- Decision Tree classification Algorithm.
- Random Forest Classification Algorithm.
- Logistic Classification Algorithm.


## Introduction:

### Data Description:

In astronomy, stellar classification is the classification of stars based on their spectral characteristics. The classification scheme of galaxies, quasars, and stars is one of the most fundamental in astronomy. The early cataloguing of stars and their distribution in the sky has led to the understanding that they make up our own galaxy and, following the distinction that Andromeda was a separate galaxy to our own, numerous galaxies began to be surveyed as more powerful telescopes were built. This datasat aims to classificate stars, galaxies, and quasars based on their spectral characteristics.


### Data Content:

The data consists of observations of space taken by the SDSS (Sloan Digital Sky Survey). Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.


### Data Dictionary:

- obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS
- alpha = Right Ascension angle (at J2000 epoch)
- delta = Declination angle (at J2000 epoch)
- u = Ultraviolet filter in the photometric system
- g = Green filter in the photometric system
- r = Red filter in the photometric system
- i = Near Infrared filter in the photometric system
- z = Infrared filter in the photometric system
- run_ID = Run Number used to identify the specific scan
- rereun_ID = Rerun Number to specify how the image was processed
- cam_col = Camera column to identify the scanline within the run
- field_ID = Field number to identify each field
- spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)
- class = object class (galaxy, star or quasar object)
- redshift = redshift value based on the increase in wavelength
- plate = plate ID, identifies each plate in SDSS
- MJD = Modified Julian Date, used to indicate when a given piece of SDSS
- fiber_ID = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation

## Exploratory Data Analysis (EDA):

### Data Cleaning:
- Drop [Unnamed: 0] column.
- Change ID Fields data type to Object.
- Drop row #76965 because it has negative values.


## Algorithms Results:
- K-nearest Neighbors Algorithm: Accuracy = 0.94
- Decision Tree classification Algorithm: Accuracy = 0.974
- Random Forest Classification Algorithm: Accuracy = 0.968
- Logistic Classification Algorithm: Accuracy =0.93


## Conclusion:

For This dataset the best preformed algorithm was Decision Tree classification Algorithm with the Accuracy of 97.4%


