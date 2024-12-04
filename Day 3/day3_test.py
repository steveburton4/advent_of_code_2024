from day3 import read_input, find_valid_mul_statements, get_total_of_single_mul_statement
from day3 import get_total_of_mul_statements, find_all_enabled_sections, find_valid_mul_statements_from_list_text

def test_day_3_read_valid_input():
    expected = "why()}''(!how()$~mul(420,484) ]}}don't()mul(218,461),]/select()do()mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);don't()mul(97,699)select()+%when()~who():mul(387,15)>do()mul(927,207)~>~when()*who()'mul(454,740"
    actual = read_input('Day 3/test_input.txt')
    assert expected == actual

def test_day_3_find_valid_amount_of_mul_statements():
    input_text = "why()}''(!how()$~mul(420,484) ]}}don't()mul(218,461),]/select()do()mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);don't()mul(97,699)select()+%when()~who():mul(387,15)>do()mul(927,207)~>~when()*who()'mul(454,740"
    expected = 8
    actual = find_valid_mul_statements(input_text)
    assert expected == len(actual)

def test_day_3_find_valid_mul_statements():
    input_text = "why()}''(!how()$~mul(420,484) ]}}don't()mul(218,461),]/select()do()mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);don't()mul(97,699)select()+%when()~who():mul(387,15)>do()mul(927,207)~>~when()*who()'mul(454,740"
    expected = ['mul(420,484)', 'mul(218,461)', 'mul(162,415)', 'mul(556,374)', 'mul(561,946)', 'mul(97,699)', 'mul(387,15)', 'mul(927,207)']
    actual = find_valid_mul_statements(input_text)
    assert expected == actual

def test_day_3_find_valid_amount_of_all_enabled_sections():
    input_text = "why()}''(!how()$~mul(420,484) ]}}don't()mul(218,461),]/select()do()mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);don't()mul(97,699)select()+%when()~who():mul(387,15)>do()mul(927,207)~>~when()*who()'mul(454,740"
    expected = 3
    actual = find_all_enabled_sections(input_text)
    assert expected == len(actual)

def test_day_3_find_all_enabled_sections():
    input_text = "why()}''(!how()$~mul(420,484) ]}}don't()mul(218,461),]/select()do()mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);don't()mul(97,699)select()+%when()~who():mul(387,15)>do()mul(927,207)~>~when()*who()'mul(454,740"
    expected = ["why()}''(!how()$~mul(420,484) ]}}", "mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);", "mul(927,207)~>~when()*who()'mul(454,740"]
    actual = find_all_enabled_sections(input_text)
    assert expected == actual

def test_day_3_find_valid_mul_statements_from_list_text():
    input_list = ["why()}''(!how()$~mul(420,484) ]}}", "mul(93,a6)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);", "mul(927,207)~>~when()*who()'mul(454,740"]
    expected = ['mul(420,484)', 'mul(162,415)', 'mul(556,374)', 'mul(561,946)', 'mul(927,207)']
    actual = find_valid_mul_statements_from_list_text(input_list)
    assert expected == actual

def test_day_3_get_total_of_valid_mul_statement():
    input_text = 'mul(420,484)'
    expected = 203280
    actual = get_total_of_single_mul_statement(input_text)
    assert expected == actual

def test_day_3_get_total_of_valid_mul_statements():
    input_list = ['mul(420,484)', 'mul(218,461)', 'mul(162,415)']
    expected = 371008
    actual = get_total_of_mul_statements(input_list)
    assert expected == actual
