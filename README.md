# Thigh Sarcoma Auto-Segmentation Tool

Automated segmentation of thigh soft tissue sarcoma and surrounding anatomical structures from MRI using nnU-Net.

## Purpose

This tool provides automated segmentation of key anatomical structures in thigh MRI to support pre-operative surgical planning and facilitate intra-operative imaging deployment for soft tissue sarcoma cases.

## Segmented Structures

| Label | Structure |
|-------|----------|
| 1 | Skin |
| 2 | Subcutaneous tissue |
| 3 | Femur |
| 4 | Femoral vascular bundle |
| 5 | Tumour |
| 6 | Rectus femoris |
| 7 | Vastus lateralis |
| 8 | Iliotibial band |
| 9 | Biceps femoris |
| 10 | Gracilis |

## Performance

Evaluated on two separate test sets (n=5 each), excluding skin:

| Test Set | Mean Dice |
|----------|----------|
| Same acquisition protocol | 0.80 |
| Different acquisition protocol | 0.52 |

## Installation

1. Install dependencies: `pip install -r requirements.txt`
2. Download model weights: `python download_model.py`

## Usage

```
python predict.py -i /path/to/input -o /path/to/output
```

Input files must be NIfTI format named with the _0000 suffix (e.g. patient001_0000.nii.gz).

## Training Details

- Framework: nnU-Net v2 (3d_fullres)
- Training cases: 50 manually segmented / InteractiveNET-assisted thigh MRIs
- Imaging: Predominantly T1-weighted, some T2-weighted
- Input: Single-channel MRI (.nii.gz)

## Citation

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., and Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

## License

MIT License
