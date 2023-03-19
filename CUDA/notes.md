# Video CUDA Jetson

you can divise CUDA in 2 major parts:
- CUDA toolkit help devs build and debug apps:
  - Libraries (image processing and math)
  - Devtools (profiler and debugger)
  - CUDA runtime API
  - Versioned in a.b format (11.4)
- CUDA driver : User-Mode library for access to "Driver API"
  - Part of the NVIDIA Jetson Linux - Board support package / BSP for Jetson device


CUDA compatibility
  - backward compatibility: 
    - the CUDA driver maintains backward compatibility to continue support of apps built on older toolkits
    - GPU drivers will be binary compatible with older binaries
    - Recompiling from source  may need API changes
  - Minor-version compatibility
    - Applications created within a major-release of CUDA may run on a system  with the minimum driver version
  - Forward compatibility

Lazy loading (use less memory)