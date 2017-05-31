
echo -e '\n\n	== == FCN == ==\n'

python test_fcn32_vgg.py
#python test_fcn16_vgg.py
#python test_fcn8_vgg.py

find . -name "*.pyc" -type f -delete

