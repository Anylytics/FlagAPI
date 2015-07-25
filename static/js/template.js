// Now we've configured RequireJS, we can load our dependencies and start
define([ 'ractive', 'rv!../ractive/template'], function ( Ractive, html) {



    var sampleRactive = new Ractive({
      el: 'ractiveDiv',
      template: html,
      data: {
        greeting: "Hello, World"
      }
    });

    return sampleRactive;

});
