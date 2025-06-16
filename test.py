from huggingface_hub import snapshot_download
import os
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

snapshot_download(
    repo_id="gjliu/V2Xverse",
    repo_type="dataset",
    local_dir="./dataset",
    token='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',
    resume_download=True  # 支持断点续传
)
print(1)
