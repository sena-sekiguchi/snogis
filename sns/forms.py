from django import forms
from.models import Message,Group,Friend,Good,Menber,Category
from django.contrib.auth.models import User


# Messageのフォーム（未使用）
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner','group','content']

# Groupのフォーム（未使用）
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['owner', 'title']

# Friendのフォーム（未使用）
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner', 'user', 'group']

# Goodのフォーム（未使用）
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'message']

# Groupのチェックボックスフォーム
class GroupCheckForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupCheckForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.MultipleChoiceField(
            choices=[(item.title, item.title) for item in \
                Group.objects.filter(owner__in=[user,public])],
            widget=forms.CheckboxSelectMultiple(),
        )

# Groupの選択メニューフォーム
class GroupSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupSelectForm, self).__init__(*args, **kwargs)
        self.fields['groups'] = forms.ChoiceField(
            choices=[('-','-')] + [(item.title, item.title) \
                for item in Group.objects.filter(owner=user)],
                widget=forms.Select(attrs={'class':'form-control'}),
        )

# Friendのチェックボックスフォーム
class FriendsForm(forms.Form):
    def __init__(self, user, friends=[], vals=[], *args, **kwargs):
        super(FriendsForm, self).__init__(*args, **kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
            choices=[(item.user, item.user) for item in friends],
            widget=forms.CheckboxSelectMultiple(),
            initial=vals
        )

# Group作成フォーム
class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=50, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
 

# 投稿フォーム
class PostForm(forms.Form):
    
    CATEGORY_CHOICES = (
    ('TV','TV'),
    ('ラジオ','ラジオ'),
    ('雑誌','雑誌'),
    ('ブログ','ブログ'),
    ('モバメ','モバメ'),
    )
    #category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    menber = forms.ModelChoiceField(queryset=Menber.objects.all(),label="メンバー")
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label="カテゴリー")
    STAR_CHOICES = (
    (5,5),
    (4,4),
    (3,3),
    (2,2),
    (1,1),
    )   
    star = forms.ChoiceField(choices=STAR_CHOICES,label="星")
    content = forms.CharField(max_length=500, \
    widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}),label="投稿内容")

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
