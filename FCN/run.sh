
echo -e '\n\n	== == FCN32 == ==\n'
python test_fcn32_vgg.py

echo -e '\n\n	== == FCN16 == ==\n'
python test_fcn16_vgg.py

echo -e '\n\n	== == FCN8 == ==\n'
python test_fcn8_vgg.py

find . -name "*.pyc" -type f -delete

