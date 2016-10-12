import sublime, sublime_plugin

STORED_SETTINGS = {}

class nomin(sublime_plugin.TextCommand):
    def run(self, edit):

        view = self.view
        settings = view.settings()

        if settings.get("is_widget"):
            return

            if view.file_name():
                viewID = view.file_name()
            else:
                viewID = str(view)

                global STORED_SETTINGS
                if not viewID in STORED_SETTINGS:
                    STORED_SETTINGS[ viewID ] = {
                    "minified_source_indexing_disabled": True,
                    "binary_file_patterns": settings.get( "binary_file_patterns"),
                    }
                    storedSettings = STORED_SETTINGS[ viewID ]

                    if storedSettings[ "minified_source_indexing_disabled" ]:
                        settings.set( "binary_file_patterns", ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.ttf", "*.tga", "*.dds", "*.ico", "*.eot", "*.pdf", "*.swf", "*.jar", "*.zip", "min/*", "node_modules/*" "*.min*"] )
                    else:
                        settings.set( "binary_file_patterns", storedSettings[ "binary_file_patterns" ] )

                        storedSettings[ "minified_source_indexing_disabled" ] = not storedSettings[ "minified_source_indexing_disabled" ]

                    print(storedSettings);