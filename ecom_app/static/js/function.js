<script>
            function call_counter(pk) {
                window.open(url);
                $.get('YOUR_VIEW_HERE/'+pk+'/', function (data) {
                    alert("counter updated!");
                });
            }
</script>