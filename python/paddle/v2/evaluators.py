# Copyright (c) 2016 PaddlePaddle Authors. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle.trainer_config_helpers.evaluators as evs
import inspect
from config_base import __convert_to_v2__

__all__ = []


def initialize():
    for __ev_name__ in filter(lambda x: x.endswith('_evaluator'), evs.__all__):
        __ev__ = getattr(evs, __ev_name__)
        if hasattr(__ev__, 'argspec'):
            argspec = __ev__.argspec
        else:
            argspec = inspect.getargspec(__ev__)
        parent_names = filter(lambda x: x in ['input', 'label'], argspec.args)
        v2_ev = __convert_to_v2__(
            __ev_name__,
            parent_names=parent_names,
            is_default_name='name' in argspec.args,
            attach_parent=True)
        globals()[__ev_name__] = v2_ev
        globals()[__ev_name__].__name__ = __ev_name__
        __all__.append(__ev_name__)


initialize()
