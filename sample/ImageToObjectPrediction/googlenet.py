# Copyright (c) 2015 Preferred Infrastructure, Inc.
# Copyright (c) 2015 Preferred Networks, Inc.Permission is hereby granted,
# free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"),
# to deal in the Software without restriction,
# including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.THE SOFTWARE IS PROVIDED
# "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import chainer
import chainer.functions as F
import chainer.links as L


class GoogLeNet(chainer.Chain):

    insize = 224

    def __init__(self):
        super(GoogLeNet, self).__init__(
            conv1=L.Convolution2D(3,  64, 7, stride=2, pad=3),
            conv2_reduce=L.Convolution2D(64,  64, 1),
            conv2=L.Convolution2D(64, 192, 3, stride=1, pad=1),
            inc3a=L.Inception(192,  64,  96, 128, 16,  32,  32),
            inc3b=L.Inception(256, 128, 128, 192, 32,  96,  64),
            inc4a=L.Inception(480, 192,  96, 208, 16,  48,  64),
            inc4b=L.Inception(512, 160, 112, 224, 24,  64,  64),
            inc4c=L.Inception(512, 128, 128, 256, 24,  64,  64),
            inc4d=L.Inception(512, 112, 144, 288, 32,  64,  64),
            inc4e=L.Inception(528, 256, 160, 320, 32, 128, 128),
            inc5a=L.Inception(832, 256, 160, 320, 32, 128, 128),
            inc5b=L.Inception(832, 384, 192, 384, 48, 128, 128),
            loss3_fc=L.Linear(1024, 1000),

            loss1_conv=L.Convolution2D(512, 128, 1),
            loss1_fc1=L.Linear(2048, 1024),
            loss1_fc2=L.Linear(1024, 1000),

            loss2_conv=L.Convolution2D(528, 128, 1),
            loss2_fc1=L.Linear(2048, 1024),
            loss2_fc2=L.Linear(1024, 1000)
        )
        self.train = True

    def __call__(self, x):
        h = F.relu(self.conv1(x))
        h = F.local_response_normalization(
            F.max_pooling_2d(h, 3, stride=2), n=5, k=1, alpha=2e-05)
        h = F.relu(self.conv2_reduce(h))
        h = F.relu(self.conv2(h))
        h = F.max_pooling_2d(
            F.local_response_normalization(h, n=5, k=1, alpha=2e-05), 3, stride=2)

        h = self.inc3a(h)
        h = self.inc3b(h)
        h = F.max_pooling_2d(h, 3, stride=2)
        h = self.inc4a(h)

        l = F.average_pooling_2d(h, 5, stride=3)
        l = F.relu(self.loss1_conv(l))
        l = F.relu(self.loss1_fc1(l))
        l = self.loss1_fc2(l)

        h = self.inc4b(h)
        h = self.inc4c(h)
        h = self.inc4d(h)

        l = F.average_pooling_2d(h, 5, stride=3)
        l = F.relu(self.loss2_conv(l))
        l = F.relu(self.loss2_fc1(l))
        l = self.loss2_fc2(l)

        h = self.inc4e(h)
        h = F.max_pooling_2d(h, 3, stride=2)
        h = self.inc5a(h)
        h = self.inc5b(h)

        h = F.average_pooling_2d(h, 7, stride=1)
        y = self.loss3_fc(F.dropout(h, 0.4))

        return y
