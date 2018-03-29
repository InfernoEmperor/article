<script type="text/javascript">
    //修改现有的class
    $(function () {
        $(".detail").addClass("selected");
    })
    //添加回调事件
    $(function() {
        if($(".filePicker").length > 0){
            // 绑定选择事件
            $(".filePicker").bind("click", function(e){
                $("#fileImage").click();
            });
        }
    })
    //文件打开后
    document.querySelector('#fileImage').addEventListener('change', function(){

        //实例化一个FileReader
        var reader = new FileReader();

        reader.onload = function (e) {
            var fileName = getfilename();
            var fileArray = fileName.split(".");
            var type = fileArray[fileArray.length - 1].toLocaleLowerCase();
            if (type == 'jpg' || type == 'png') {
                if (!$('#mainImage').attr('src')) {
                    document.querySelector('#mainImage').src = e.target.result;
                    $('#stepInfo').html("请选择副图！");
                }
                else {
                    if (!$('#assistImage').attr('src')) {
                        document.querySelector('#assistImage').src = e.target.result;
                        $('#stepInfo').html("点击上传按钮进行提交！");
                    }
                    else {
                        $('#stepInfo').html("请先删除选择");
                    }
                }
            } else {
                $('#stepInfo').html("请输入jpg或者png格式的图片!");
            }
        };
    //读取选中的图片，并转换成dataURL格式
    reader.readAsDataURL(this.files[0]);
    }, false);

    document.ondragover = function (e) {
        e.preventDefault();
    };
    document.ondrop = function (e) {
        e.preventDefault();      
    };

    var oDiv = $('#fileDragArea').get(0);
    oDiv.ondragover = function (e) {
        e.preventDefault();
        $(this).addClass("upload_drag_hover");
    };
    oDiv.ondrop = function (e) {
        e.preventDefault();
        $(this).removeClass("upload_drag_hover");
        var file = e.dataTransfer.files[0];
        var _type = file.type;
        if (_type.indexOf('image') != -1) {
            var reader =  new FileReader();
            reader.readAsDataURL(file);

            reader.onload = function(e) {
                if (!$('#mainImage').attr('src')) {
                    document.querySelector('#mainImage').src = e.target.result;
                    $('#stepInfo').html("请选择副图！");
                }
                else {
                    if (!$('#assistImage').attr('src')) {
                        document.querySelector('#assistImage').src = e.target.result;
                        $('#stepInfo').html("点击上传按钮进行提交！");
                    }
                    else {
                        $('#stepInfo').html("请先删除选择");
                    }
                }
            }
            reader.onloadend = function() {
                if (reader.error) {
                    $('#stepInfo').html(reader.error);
                } else {
                    //上传二进制
                    console.info("上传成功！");
                }
            }
            
        } else {
            $('#stepInfo').html("请输入jpg或者png格式的图片!");
        }
            
    }
    
    function getfilename(){
        var file = $("#fileImage").val();
        var pos=file.lastIndexOf("\\");
        return file.substring(pos+1);  
    }
    $(function () {
        var clear_btn = document.getElementById("clear_btn");
        var upload_btn = document.getElementById("upload_btn");

        clear_btn.onclick = function(e) {
            document.querySelector('#mainImage').src = "";
            document.querySelector('#assistImage').src = "";
            $('#stepInfo').html("请选择一张主图片!");
        }
        upload_btn.onclick = function(e) {
            document.querySelector('#mainImage').src = "";
            document.querySelector('#assistImage').src = "";
            $('#stepInfo').html("图片已上传，请不要关闭页面，耐心等待结果！");
        }

    })
</script>