	var $schedule_count = 1;

	function form_add_classroom_send()
	{
		$('#form_add_classroom').submit();
	}

	function form_add_schedule()
	{
		$('#form_schedule_add_schedule').before("<tr id='form_schedule_"+$schedule_count+"'> \
				<td><select name='schedule-"+$schedule_count+"-day'> \
					<option value='1'>Lunes</option> \
					<option value='2'>Martes</option> \
					<option value='3'>Miércoles</option> \
					<option value='4'>Jueves</option> \
					<option value='5'>Viernes</option> \
				</select></td> \
				<td><input type='text' name='schedule-"+$schedule_count+"-start_hour'></td> \
				<td><input type='text' name='schedule-"+$schedule_count+"-end_hour'></td> \
				<td class='form_schedule_delete_button_td'><div class='form_button' onclick='form_delete_schedule("+$schedule_count+")'>Eliminar</div> \
				</td> \
		</tr>");
		$schedule_count++;
	}

	function form_delete_schedule($id_schedule)
	{
		$('#form_schedule_'+$id_schedule).remove();
	}