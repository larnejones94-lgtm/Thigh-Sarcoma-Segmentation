import argparse
import os
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Thigh Sarcoma Auto-Segmentation")
    parser.add_argument("-i", "--input", required=True, help="Input folder with NIfTI files")
    parser.add_argument("-o", "--output", required=True, help="Output folder for predictions")
    args = parser.parse_args()

    repo_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(repo_dir, "nnUNet_results")
    checkpoint = os.path.join(results_dir, "Dataset001_ThighMRI",
                              "nnUNetTrainer__nnUNetPlans__3d_fullres",
                              "fold_all", "checkpoint_final.pth")

    if not os.path.exists(checkpoint):
        print("Model weights not found. Run python download_model.py first.")
        sys.exit(1)

    os.environ["nnUNet_results"] = results_dir
    os.makedirs(args.output, exist_ok=True)

    cmd = [
        sys.executable, "-m", "nnunetv2.inference.predict_from_raw_data",
        "-i", args.input,
        "-o", args.output,
        "-d", "1",
        "-c", "3d_fullres",
        "-f", "all"
    ]

    print("Running prediction...")
    subprocess.run(cmd, check=True)
    print(f"Predictions saved to {args.output}")

if __name__ == "__main__":
    main()
