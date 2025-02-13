from src.input_cell import InputCellString

access_data = {
    'ariel.flores1@mx.nestle.com':{
        'template':[InputCellString(cell_name='KPI',
                                    validate_dict={'Validate':True,'Patter':r"^KPI\d{1,}"}),
                               InputCellString(cell_name='Year-Month',
                                              validate_dict={'Validate':True,'Patter':r"^\d{4}(0[1-9]|1[0-2])$"})],
        'columns':['KPI','Year-Month']
    },
    'fernando.lerios1@mx.nestle.com':{
        'template':[InputCellString(cell_name='KPI',validate_dict={'Validate':True,'Patter':r"^KPI\d{1,}"})],
        'columns':['KPI']
    }

}
