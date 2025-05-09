##FLARE

## Installation and Usage 🚀

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/musteryasm/FLARE.git
   cd Real-Time-Smoke-Fire-Detection-YOLO11
   ```

2. Install the required packages:
   ```bash
   pip install ultralytics
   ```

### Inference

To perform inference with the trained model on test images, run:

```bash
yolo detect predict model=models/best_nano_111.pt source=data/house.png conf=0.35 iou=0.1
```

and there's the output:

<div align='center'>
<img src="data/ex4.png" alt="Example 1" width="700"/> 
</div>

To perform inference in real-time using a webcam:

```bash
yolo detect predict model=models/best_nano_111.pt source=0 conf=0.35 iou=0.1 show=True
```

---

<div align="center">

**Protect What Matters Most - Early Detection Saves Lives**

</div>
