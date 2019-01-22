(function($) {
     $(function(){
           $('.adminfilespicker').each(
               function(){
	           var href = '/adminfiles/all/?field='+this.id;
	           if (this.options) {
		       $(this).siblings('a.add-another').remove();
		       href += '&field_type=select';
	           }
	           $(this).after('<label>Adminfiles:</label> <iframe frameborder="0" class="adminfiles-gallery" src="' + href + '"></iframe>');
	       });
       });
 })(jQuery);
