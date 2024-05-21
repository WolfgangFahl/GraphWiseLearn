"""
Created on 2024-05-21

@author: wf
"""
from dataclasses import dataclass

import graphwiselearn


@dataclass
class Version:
    """
    Version handling for graphwiselearn
    """

    name = "GraphWiseLearn"
    version = graphwiselearn.__version__
    date = "2024-05-21"
    updated = "2024-05-21"
    description = ""

    authors = "Wolfgang Fahl"

    doc_url = "https://wiki.bitplan.com/index.php/GraphWiseLearn"
    chat_url = "https://github.com/WolfgangFahl/GraphWiseLearn/discussions"
    cm_url = "https://github.com/WolfgangFahl/GraphWiseLearn"

    license = f"""Copyright 2024 contributors. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied."""

    longDescription = f"""{name} version {version}
{description}

  Created by {authors} on {date} last updated {updated}"""
