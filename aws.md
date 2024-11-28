```sh
cd mekongai/saves 

aws s3 cp checkpoints.zip s3://bucket-comfyui/saves/checkpoints.zip

### dowload
aws s3 cp s3://bucket-comfyui/saves/clip_vision.zip .

# backup mekongai
aws s3 cp /mekongai s3://mekongai --recursive

# xóa thùng rác
rm -rf ~/.local/share/Trash/*

# upload lên s3
aws s3 cp mekongai s3://mekongai/ --recursive --profile MAIN
aws s3 cp mekongai s3://playpikk/ --recursive --profile AUGFY
aws s3 cp mekongai s3://new-bucket-2fda1afe/ --recursive --profile HNLSRQ
aws s3 cp mekongai s3://cdn.leadiffer.cn/tests/ --recursive

# update thay đổi lên s3
aws s3 sync mekongai s3://mekongai/ --exact-timestamps --profile MAIN
aws s3 sync mekongai s3://playpikk/ --exact-timestamps --profile AUGFY
aws s3 sync mekongai s3://new-bucket-2fda1afe/ --exact-timestamps --profile HNLSRQ
aws s3 sync mekongai s3://cdn.leadiffer.cn/tests/ --exact-timestamps

# Xem ls s3
aws s3 ls --profile MAIN
aws s3 ls s3://playpikk --profile AUGFY
aws s3 ls s3://new-bucket-2fda1afe --profile HNLSRQ
aws s3 ls s3://cdn.leadiffer.cn/tests

# Download về
aws s3 cp s3://mekongai/ mekongai/ --recursive --profile MAIN


```


### 
```sh
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_004_model_1/flux_lora_product_004_model_1.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_004_model_2/flux_lora_product_004_model_2.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_005_model_1/flux_lora_product_005_model_1_000018500.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_005_model_2/flux_lora_product_005_model_2_000018500.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_006_model_1/flux_lora_product_006_model_1_000014000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_006_model_2/flux_lora_product_006_model_2_000015000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_006_model_2_custom_2/flux_lora_product_006_model_2_custom_2_000016000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_005_model_2_custom_2/flux_lora_product_005_model_2_custom_2_000018500.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_006_model_2_custom_2/flux_lora_product_006_model_2_custom_2_000014000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ




aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_008_model_1/flux_lora_product_008_model_1_000019000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_014_model_3/flux_lora_product_014_model_3.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_012_model_2/flux_lora_product_012_model_2_000009000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_007_model_1/flux_lora_product_007_model_1_000012000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_017_model_3/flux_lora_product_017_model_3.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_013_model_1/flux_lora_product_013_model_1.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ


aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_006/flux_lora_product_006.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_007/flux_lora_product_007.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_008/flux_lora_product_008.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_012/flux_lora_product_012.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_013/flux_lora_product_013.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_014/flux_lora_product_014.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_017/flux_lora_product_017.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_021/flux_lora_product_021.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_020/flux_lora_product_020.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_022/flux_lora_product_022.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_026/flux_lora_product_026.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ


aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_product_026/flux_lora_product_026.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ




aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_020/flux_lora_tight_020_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_020/flux_lora_tight_020.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_007/flux_lora_tight_007_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_007/flux_lora_tight_007.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_014/flux_lora_tight_014_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_014/flux_lora_tight_014.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
+
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_012/flux_lora_tight_012_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_012/flux_lora_tight_012.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_005/flux_lora_tight_005_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_005/flux_lora_tight_005.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_006/flux_lora_tight_006_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_006/flux_lora_tight_006.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_008/flux_lora_tight_008_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_008/flux_lora_tight_008.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ

aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_004/flux_lora_tight_004_000011000.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ
aws s3 cp /home/ubuntu/mekongai/ai-toolkit/output/flux_lora_tight_004/flux_lora_tight_004.safetensors s3://new-bucket-2fda1afe/flux/ --profile HNLSRQ



flux_lora_tight_020_000011000.safetensors 
flux_lora_tight_020.safetensors 

flux_lora_tight_007_000011000.safetensors 
flux_lora_tight_007.safetensors 

flux_lora_tight_014_000011000.safetensors 
flux_lora_tight_014.safetensors 
+
flux_lora_tight_012_000011000.safetensors 
flux_lora_tight_012.safetensors 

flux_lora_tight_005_000011000.safetensors 
flux_lora_tight_005.safetensors 

flux_lora_tight_006_000011000.safetensors 
flux_lora_tight_006.safetensors 

flux_lora_tight_008_000011000.safetensors 
flux_lora_tight_008.safetensors 

flux_lora_tight_004_000011000.safetensors 
flux_lora_tight_004.safetensors 

#
aws s3 sync s3://new-bucket-2fda1afe/flux/ /home/ubuntu/mekongai/saves/lora/flux/ --profile HNLSRQ
aws s3 sync s3://new-bucket-2fda1afe/flux/ /data/saves/loras/flux/ --profile HNLSRQ

aws s3 sync s3://mekongai/saves/ /home/ubuntu/mekongai/saves/ --profile MAIN
```