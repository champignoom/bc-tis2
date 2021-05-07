import json
import sys
from pathlib import Path


config = [
    {
        "name" : Path(f).stem,
        "filesystem": {
            "files": [
                {
                    "name": "tis-mkfs-stdin",
                    "from": f
                    }
                ]
            },
        "val-args": " -l",
        "include": "tis-common.config"
    } for f in sys.argv[1:]
]

print(json.dumps(config, sort_keys=True, indent=4))
