var disqus_config = function () {
this.page.url = 'http://localhost:8000/blog/{{url}}/';
this.page.identifier = '{{url}}';
};

(function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://rootxyz.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();
