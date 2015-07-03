// Магія розпочнеться лише після повного завантаження сторінки
$(document).ready(function () {
	setCommentsHandlers();
	
	$('.response_default').click(function()  {
		$('#comment_text').html('Новый комментарий');
		$('#id_last_comment').val(0);
		console.log('response_default');
		return false; //запрещаем переход по ссылке
	});

    // Посилання з id="test" буде тригером події
    // $("#test_comment").click(function() {
    //     // AJAX-запит на потрібну адресу
    //     var id_comment = $('#id_comment:value')
    //     $.post("/ajax_test/", {'id_comment': 'id_comment'}, function(data) {
    //         // Замінюємо текст тегу з id="target" на отримані дані
    //         $("#target_comment").html(data.param1+' '+data.param2);
    //     });
    // });
	
	
	$('.new_power_comment').submit(function(e){
		//отменяем стандартное действие при отправке формы
		e.preventDefault();
		//берем из формы метод передачи данных
		var m_method=$(this).attr('method');
		//получаем адрес скрипта на сервере, куда нужно отправить форму
		var m_action=$(this).attr('action');

		var m_data=$(this).serialize();
		var thisForm = $(this);

		$.ajax({
			type: m_method,
			url: m_action,
			data: m_data,
			success: function(data){
				if (data.success == false){
					$('#new_comment_form').addClass("has-error");
					$('#comment_alert_dander').show()
					$('#comment_alert_dander').html(data.message)
				} else {
					$('#new_comment_form').removeClass("has-error");
					$('#comment_alert_dander').hide()
					$('#id_text_comment').val("");
					$('#power_comments').html(data);
					setCommentsHandlers();
				}
			}
		});
	});
});

function setCommentsHandlers(){
	$('.rating_form_minus').submit(function(e){
		//отменяем стандартное действие при отправке формы
		e.preventDefault();
		//берем из формы метод передачи данных
		var m_method=$(this).attr('method');
		//получаем адрес скрипта на сервере, куда нужно отправить форму
		var m_action=$(this).attr('action');

		//получаем данные, введенные пользователем в формате input1=value1&input2=value2...,
		//то есть в стандартном формате передачи данных формы
		var m_data=$(this).serialize();
		var thisForm = $(this);
		// var id_click = console.log(e.target);
		// var id_click =   e.target.id;
		// alert(id_click)
		// Получаем всю форму
		// var m_data = $("form").serialize();
		$.ajax({
			type: m_method,
			url: m_action,
			data: m_data,
			success: function(result){
				$('.comment_rating-'+result.id_comment).html(result.rating);
			}
			});
	});

	$('.rating_form_plus').submit(function(e){
		e.preventDefault();
		var m_method=$(this).attr('method');
		var m_action=$(this).attr('action');
		var m_data=$(this).serialize();
		var thisForm = $(this);
		console.log(m_method, m_action, m_data);
		$.ajax({
			type: m_method,
			url: m_action,
			data: m_data,
			success: function(result){
				console.log(result.rating, result.id_comment);
				$('.comment_rating-'+result.id_comment).html(result.rating);
			}
		});		
	});

	$('.responce_comment').click(function()  {
		var id = parseInt($(this).attr('id').split('-')[1]); //находим id
		var user_name = $('#comment-'+id).attr('title');
		// $('#id_text_comment').val(user_name+', ');
		$('#comment_text').html('Ответ пользователю: '+user_name);

		// var title = $(this).attr('title');
		$('#id_last_comment').val(id);
		console.log('responce_comment');
		// return false; //запрещаем переход по ссылке
	});
}