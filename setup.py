from setuptools import setup, find_packages

setup(
  name = 'GeneSplice',
  packages = find_packages(exclude=[]),
  version = '0.0.2',
  license='MIT',
  description = 'GeneSplice Model, Ultra-Long Rage Genomic Expression Modelling',
  author = 'Kye Gomez',
  author_email = 'kye@apac.ai',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/kyegomez/GeneSplice',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'long context',
    'genomics',
    'pre-training'
  ],
  install_requires=[
      'torch',
      'einops',
      'transformers',
      'accelerate',
      'fairscale',
      'timm',
      'flash-attn',
    ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)