from setuptools import find_packages, setup

setup(
    name='yolo_core',
    packages=find_packages(include=['core']),
    version='0.1.0',
    description='Python wrapper for YOLO Real-Time ObjectDetection Library',
    author='Paul Jeremiah Mugaya',
    install_requires=['tensorflow', 'pytesseract', 'easydict', 'opencv-python==4.1.1.26'],
    license='MIT',
)
