import os
from huggingface_hub import hf_hub_download

REPO_ID = "larnejones94/thigh-sarcoma-segmentation"
FILENAME = "checkpoint_final.pth"

dest = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "nnUNet_results", "Dataset001_ThighMRI",
    "nnUNetTrainer__nnUNetPlans__3d_fullres", "fold_all"
)

print(f"Downloading model weights to {dest}...")
hf_hub_download(
    repo_id=REPO_ID,
    filename=FILENAME,
    local_dir=dest,
    local_dir_use_symlinks=False
)
print("Done!")
