	var $input_count = 2;

	function form_add_input()
	{
		$('#form_input_add_input').before("<tr id='form_input_"+$input_count+"'> \
				<td><input type='text' name='input-"+$input_count+"-name'></td> \
				<td class='form_schedule_delete_button_td'><div class='form_button' onclick='form_delete_input("+$input_count+")'>Eliminar</div> \
			</tr>");
		$input_count++;
	}

	function form_delete_input($id_input)
	{
		$('#form_input_'+$id_input).remove();
	}