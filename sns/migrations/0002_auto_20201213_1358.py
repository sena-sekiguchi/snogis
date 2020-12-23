# Generated by Django 3.1.4 on 2020-12-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='menber',
            field=models.CharField(choices=[('秋元真夏', '秋元真夏'), ('生田絵梨花', '生田絵梨花'), ('伊藤純奈', '伊藤純奈'), ('伊藤理々杏', '伊藤理々杏'), ('岩本蓮加', '岩本蓮加'), ('梅澤美波', '梅澤美波'), ('大園桃子', '大園桃子'), ('北野日奈子', '北野日奈子'), ('久保史緒里', '久保史緒里'), ('齋藤飛鳥', '齋藤飛鳥'), ('阪口珠美', '阪口珠美'), ('佐藤楓', '佐藤楓'), ('新内眞衣', '新内眞衣'), ('鈴木絢音', '鈴木絢音'), ('高山一実', '高山一実'), ('寺田蘭世', '寺田蘭世'), ('中村麗乃', '中村麗乃'), ('樋口日奈', '樋口日奈'), ('星野みなみ', '星野みなみ'), ('堀未央奈', '堀未央奈'), ('松村沙友理', '松村沙友理'), ('向井葉月', '向井葉月'), ('山崎怜奈', '山崎怜奈'), ('山下美月', '山下美月'), ('吉田綾乃クリスティー', '吉田綾乃クリスティー'), ('与田祐希', '与田祐希'), ('渡辺みり愛', '渡辺みり愛'), ('和田まあや', '和田まあや'), ('遠藤さくら', '遠藤さくら'), ('賀喜遥香', '賀喜遥香'), ('掛橋沙耶香', '掛橋沙耶香'), ('金川紗耶', '金川紗耶'), ('北川悠理', '北川悠理'), ('黒見明香', '黒見明香'), ('佐藤璃果', '佐藤璃果'), ('柴田柚菜', '柴田柚菜'), ('清宮レイ', '清宮レイ'), ('田村真佑', '田村真佑'), ('筒井あやめ', '筒井あやめ'), ('早川聖来', '早川聖来'), ('林瑠奈', '林瑠奈'), ('松尾美佑', '松尾美佑'), ('矢久保美緒', '矢久保美緒'), ('弓木奈於', '弓木奈於')], default='green', max_length=10),
        ),
    ]
