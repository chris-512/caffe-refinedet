#!/usr/bin/env python

import caffe

caffe.Net('deploy.prototxt', caffe.TEST)
