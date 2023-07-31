#!/usr/bin/env python
#-------------------------------------------------------------------------------
# The confidential and proprietary information contained in this file may
# only be used by a person authorised under and to the extent permitted
# by a subsisting licensing agreement from Arm Limited or its affiliates.
#
#        (C) COPYRIGHT 2023 Arm Limited or its affiliates.
#            ALL RIGHTS RESERVED
#
# This entire notice must be reproduced on all copies of this file
# and copies of this file may only be made by a person if such person is
# permitted to do so under the terms of a subsisting license agreement
# from Arm Limited or its affiliates.
#-------------------------------------------------------------------------------
import os
import re
from datetime import datetime
import sys
def check_copyright(file_name):
    """ Function to check for copyright. """
    if len(sys.argv) > 2:
        if sys.argv[2] == 'BSD':
            copy_right = re.compile(r".* Copyright \(c\) [\d,\-\s]*%s, Arm Limited or its affiliates\. All rights reserved\. SPDX-License-Identifier: BSD-3-Clause" % datetime.now().year)
        if sys.argv[2] == 'PSA_M':
            copy_right = re.compile(r".* Copyright \(c\) [\d,\-\s]*%s, Arm Limited or its affiliates\. All rights reserved\. SPDX-License-Identifier : Apache-2\.0.* Licensed under the Apache License, Version 2\.0 \(the \"License\"\); you may not use this file except in compliance with the License\. You may obtain a copy of the License at http://www\.apache\.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied\. See the License for the specific language governing permissions and limitations under the License\..*" % datetime.now().year)
    else:
        copy_right = re.compile(r".* Copyright \(c\) [\d,\-\s]*%s, Arm Limited or its affiliates\. All rights reserved\. SPDX-License-Identifier : Apache-2\.0 Licensed under the Apache License, Version 2\.0 \(the \"License\"\); you may not use this file except in compliance with the License\. You may obtain a copy of the License at http://www\.apache\.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied\. See the License for the specific language governing permissions and limitations under the License\..*" % datetime.now().year)
    if file_name.endswith(('.json', '.xml', '.md', '.dj', '.md5', 'yaml', '.a', '.1','.bom','.patch')) or '.gitignore' in file_name or 'groups' in file_name:
        return 0
    try:
        file_h = open(file_name, 'r')
    except (IOError) as err:
        print("ERROR-Unable to open file %s for reading : %s" %(file_name, err.strerror))
        raise
    lines = list()
    for line in file_h.readlines():
        line = line.rstrip("\n")
        line = line.rstrip()
        if re.match(r'^\s*$', line):
            continue
        match_obj = re.match(r'^\s*\W*(.*)', line)
        if match_obj: 
            replaced_str = match_obj.group(1).replace('C)', '(C)')
            lines.append(replaced_str)
        elif re.match(r'^\s*[^#/;\*].*', line):
            break
    file_h.close()
    copyright_line = ' '.join(lines)
    copyright_line = re.sub(r"\s+", " ", copyright_line)
    if not copy_right.match(copyright_line):
        print("ERROR-Copyright is not updated for file: %s" %(file_name))
        return 1
    return 0

def main(input_data):
    """ Main """
    sta = 0
    if os.path.exists(input_data):
        if os.path.isfile(input_data):
            print("os.path.isfile(input_data)")
            sta += check_copyright(input_data)
        else:
            for (dir_path, dir_name, file_names) in os.walk(input_data):
                for file_name in file_names:
                    
                    #Ignore hidden files
                    if file_name.startswith('.') or "." in dir_path:
                        continue

                    check_file = os.path.join(dir_path, file_name)
                    if os.path.isfile(check_file):
                        sta += check_copyright(check_file)
    return sta

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.exit(main(sys.argv[1]))
    else:
        print("ERROR-Please provide the file/directory path and the License it's from if it's not Apache, to check for copyright")
                                                               
