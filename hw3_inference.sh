#python tools/test_net.py --input_dir /home/guest/r11944027/val_dataset/ --out_file "/home/guest/r11944027/r11944027.json" --config-file "configs/da_faster_rcnn/test.yaml" MODEL.WEIGHT ./model_final.pth
python tools/test_net.py --input_dir "${1}" --out_file "${2}" --ckpt "${3}" --config-file "configs/da_faster_rcnn/test.yaml"
