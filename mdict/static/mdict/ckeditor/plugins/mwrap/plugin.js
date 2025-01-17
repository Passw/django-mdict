﻿CKEDITOR.plugins.add( 'mwrap', {
    icons: 'mwrap',
    init: function( editor ) {
        editor.addCommand( 'insertmwrap', {
            exec: function( editor ) {
                var text = editor.getSelection().getNative();
                editor.insertHtml( '[wrap]'+text+'[/wrap]' );
            }
        });
        editor.ui.addButton( 'mwrap', {
            label: 'insert wrap',
            command: 'insertmwrap',
            toolbar: 'insert'
        });
    }
});