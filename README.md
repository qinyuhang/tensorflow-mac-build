# Self using Tensorflow builds

## CPU only is optimized for SSE4.2 AVX AVX2

To remove the annoying message
```
2017-06-11 12:31:13.614069: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-06-11 12:31:13.614090: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-06-11 12:31:13.614095: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-06-11 12:31:13.614099: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
```
## GPU only build is try using CUDA Toolkit 8.0 + CuDNN 6 to build

PS: heard Tensorflow r1.2 will remove the CUDA support for Mac(yes well the latest Mac with NVIDA GPU is 2014 RMBP, exactly the one I am using)
