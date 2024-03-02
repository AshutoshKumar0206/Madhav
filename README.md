# madhav-ai_avatar
An AI Voice Assistant for Depression Relief: Insights from the Srimad Bhagavad Gita



$.get({
            url: 'https://en.wikipedia.org/w/api.php',
            data: {
                action: 'opensearch',
                search: 'Narendra Modi',
                format: 'json'
            },
            dataType: 'jsonp',
            success: function(response){
                console.log(response)
                results = response[1];
                $.each(results, function(index, value){
                    $("#search-ul").append("<li data-page='"+value.replace(/ /g, "_")+"'><span class='index'>"+(index+1)+"</span><div class='result'>"+value+"</div></li>")
                })

                $("#search-ul>li").on("click", function(){
                    $("#search-ul").html("")
                    $.get({
                        url: 'https://en.wikipedia.org/w/api.php',
                        data: {
                            format: 'json',
                            action: 'query',
                            prop: 'extracts',
                            exintro: null,
                            explaintext: null,
                            titles: $(this).data("page")
                        },
                        dataType: 'jsonp',
                        success: function(response){
                            var page = Object.keys(response.query.pages);
                            var extract = response.query.pages[page[0]].extract;
                            $("#search-result").html(extract)
                        }
                    })          
                })
            },
            error: function(xhr, status, error){
                console.error("Error:", error);
            }
        });