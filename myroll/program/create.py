from myroll.models import Sbj

def create():
    Sbj.objects.create(sbj_name="体育",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="芸術選択",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="化学",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="国語総合",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="歴史",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="倫理",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="総合英語1R",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="総合英語1W",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="英会話",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=16)
    Sbj.objects.create(sbj_name="数学2A",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=48)
    Sbj.objects.create(sbj_name="数学2B",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=48)
    Sbj.objects.create(sbj_name="物理1",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="化学1",std_fac="ALL",std_grd=2,curr_cnt=0,total_cnt=16)
    Sbj.objects.create(sbj_name="電気数学",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=16)
    Sbj.objects.create(sbj_name="電気回路",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="集合と論理",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=16)
    Sbj.objects.create(sbj_name="コンピュータ工学",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="プログラミング",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=32)
    Sbj.objects.create(sbj_name="プログラミング言語",std_fac="IE",std_grd=2,curr_cnt=0,total_cnt=16)