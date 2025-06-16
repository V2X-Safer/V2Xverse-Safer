from huggingface_hub import snapshot_download

# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

snapshot_download(
    repo_id="gjliu/V2Xverse",
    repo_type="dataset",
    local_dir="./",
    token="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",
    resume_download=True,
)
print(1)
