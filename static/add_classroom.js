	var $schedule_count = 2;
	var $input_count = 3;

	function form_add_classroom_send()
	{
		$('#form_add_classroom').submit();
	}

	function form_add_schedule()
	{
		$('#form_schedule_add_schedule').before("<tr id='form_schedule_"+$schedule_count+"'> \
				<td><select name='schedule_day[]'> \
					<option value='1'>Lunes</option> \
					<option value='2'>Martes</option> \
					<option value='3'>Miércoles</option> \
					<option value='4'>Jueves</option> \
					<option value='5'>Viernes</option> \
				</select></td> \
				<td><input type='text' name='schedule_start_date[]'></td> \
				<td><input type='text' name='schedule_end_date[]'></td> \
				<td class='form_schedule_delete_button_td'><div class='form_button' onclick='form_delete_schedule("+$schedule_count+")'>Eliminar</div> \
				</td> \
		</tr>");
		$schedule_count++;
	}

	function form_delete_schedule($id_schedule)
	{
		$('#form_schedule_'+$id_schedule).remove();
	}

	function form_add_input()
	{
		$('#form_input_add_input').before("<tr id='form_input_"+$input_count+"'> \
				<td><input type='text' name='input_name[]'></td> \
				<td class='form_schedule_delete_button_td'><div class='form_button' onclick='form_delete_input("+$input_count+")'>Eliminar</div> \
			</tr>");
		$input_count++;
	}

	function form_delete_input($id_input)
	{
		$('#form_input_'+$id_input).remove();
	}