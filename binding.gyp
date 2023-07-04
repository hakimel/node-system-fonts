{
    "targets": [
        {
            "target_name": "system-fonts",
            "sources": ["src/lib/FontManager.cc"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "conditions": [
                ['OS=="mac"', {
                    "sources": ["src/lib/FontManagerMac.mm"],
                    "link_settings": {
                        "libraries": ["CoreText.framework", "Foundation.framework"]
                    }
                }],
                ['OS=="win"', {
                    "sources": ["src/lib/FontManagerWindows.cc"],
                    "link_settings": {
                        "libraries": ["Dwrite.lib"]
                    }
                }]
            ]
        }
    ]
}
