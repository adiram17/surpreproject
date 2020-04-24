from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Score, Attribute, AttributeScore, Choice
from django.utils import timezone
from datetime import date
# Create your views here.

@login_required
def home(request):
    return render(request, 'pages/home.html', {})

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Pembaharuan sandi berhasil.')
            return redirect('home')
        else:
            messages.error(request, 'Pembaharuan sandi dibatalkan.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


@login_required
def score(request):
    startupname=""
    productname=""
    sentimentscore=""
    infostartupscore=""
    infoplatformscore=""
    totalscore=""
    status=""
    changeby=""
    scorecategory=""
    checked=""
    changetime=None
    calculatedate=None
    sentimentattributes=None
    infostartupattributes=None
    infoplatformattributes=None
    score = Score.objects.filter(status="DRAFT", changeby=request.user.username).first()
    choices=Choice.objects.all()
    if (score!=None):
        startupname=score.startupname
        productname=score.productname
        calculatedate=score.calculatedate
        scorecategory=score.scorecategory
        if (score.startupname==None):
            startupname=""
        if (score.productname==None):
            productname=""
        if (score.calculatedate==None):
            calculatedate=""
        if (score.scorecategory==None):
            scorecategory=""
        sentimentscore=score.sentimentscore
        infostartupscore=score.infostartupscore
        infoplatformscore=score.infoplatformscore
        totalscore=score.totalscore
        status=score.status
        changeby=score.changeby
        changetime=score.changetime
        sentimentattributes = AttributeScore.objects.all().filter(attributetype="sentiment", score_id=score.id)
        infostartupattributes = AttributeScore.objects.all().filter(attributetype="infostartup", score_id=score.id)
        infoplatformattributes = AttributeScore.objects.all().filter(attributetype="infoplatform", score_id=score.id)
    
    elif (score==None):
        newScore=Score(status="DRAFT", changeby=request.user.username)
        newScore.save()
        attributes = Attribute.objects.all()
        for attribute in attributes:
            newAttributeScore= AttributeScore(name=attribute.name, attributetype=attribute.attributetype, score_id=newScore.id)
            newAttributeScore.save()

    return render(request, 'pages/score.html', {
        'startupname':startupname, 
        'productname':productname,
        'sentimentscore':sentimentscore,
        'infostartupscore':infostartupscore,
        'infoplatformscore':infoplatformscore,
        'totalscore':totalscore,
        'status':status,
        'changeby':changeby,
        'changetime':changetime,
        'calculatedate':calculatedate,
        'sentimentattributes': sentimentattributes,
        'infostartupattributes': infostartupattributes,
        'infoplatformattributes': infoplatformattributes,
        'scorecategory': scorecategory,
        'choices': choices,
        'checked': checked,


        })

@login_required
def about(request):
    return render(request, 'pages/about.html', {})

@login_required
def scoreattribute(request):
    return render(request, 'pages/scoreattribute.html', {})

@login_required
def scorescale(request):
    return render(request, 'pages/scorescale.html', {})
    
@login_required
def scorelevel(request):
    return render(request, 'pages/scorelevel.html', {})

@login_required
def scorehistory(request):
    scores=Score.objects.filter(status="COMPLETE", changeby=request.user.username).order_by('-calculatedate')
    return render(request, 'pages/scorehistory.html', {"scores":scores})

@login_required
def test(request):
    return render(request, 'pages/test.html', {})

@csrf_protect
def getmessage(request):
    if request.method == 'POST':
        messages.success(request, 'Content Message')
        return redirect('/surpre/test')
    else:
        return redirect('/surpre/test')

def calculateScore(scoreid, attributetype):
    retval=0
    attributeScores=AttributeScore.objects.filter(score_id=scoreid, attributetype=attributetype)
    for attributeScore in attributeScores:
        retval+=attributeScore.value
    return retval

@csrf_protect
def scorepost(request):
    if request.method == 'POST':
        if ('calculate' in request.POST):
            errormessage=""
            startupname = request.POST['startupname']
            productname = request.POST['productname']
            score = Score.objects.filter(status="DRAFT", changeby=request.user.username).first()
            if (score!=None):
                #Save all attribute
                score.startupname=startupname
                score.productname=productname
                score.sentimentscore=0
                score.infostartupscore=0
                score.infoplatformscore=0
                score.totalscore=0
                score.scorecategory=None
                score.calculatedate=None
                score.save()
                attributeScores=AttributeScore.objects.filter(score_id=score.id)
                for attributeScore in attributeScores:
                    try:
                        attributeScoreValue=request.POST['inlineRadioOptions'+str(attributeScore.id)]
                        attributeScore.value=attributeScoreValue
                        attributeScore.save()
                    except:
                        print("")

                #Validation
                if (startupname=="" or startupname==None):
                    errormessage="Wajib masukkan nama startup/UMKM. "
                    messages.error(request, errormessage)
                if (productname=="" or productname==None):
                    errormessage="Wajib masukkan nama produk/UMKM. "
                    messages.error(request, errormessage)
                incompleteSentimentAttributeScores=AttributeScore.objects.filter(score_id=score.id, value=0, attributetype="sentiment").first()
                if (incompleteSentimentAttributeScores!=None):
                    errormessage="Wajib lengkapi User Sentiment State."
                    messages.error(request, errormessage)
                incompleteInfoStartupAttributeScores=AttributeScore.objects.filter(score_id=score.id, value=0, attributetype="infostartup").first()
                if (incompleteInfoStartupAttributeScores!=None):
                    errormessage="Wajib lengkapi Informasi Startup Company."
                    messages.error(request, errormessage)
                incompleteInfoPlatformAttributeScores=AttributeScore.objects.filter(score_id=score.id, value=0, attributetype="infoplatform").first()
                if (incompleteInfoPlatformAttributeScores!=None):
                    errormessage="Wajib lengkapi Informasi Platform Company."
                    messages.error(request, errormessage)
                
                #calculate here
                if (errormessage==""):
                    score.sentimentscore=calculateScore(score.id, "sentiment")
                    score.infostartupscore=calculateScore(score.id, "infostartup")
                    score.infoplatformscore=calculateScore(score.id, "infoplatform")
                    score.totalscore=score.sentimentscore+score.infostartupscore+score.infoplatformscore
                    if (score.totalscore<20):
                        score.scorecategory="Tidak Sukses"
                    elif (score.totalscore<40):
                        score.scorecategory="Sukses"
                    else:
                        score.scorecategory="Sangat Sukses"
                    score.changetime=timezone.now()
                    score.calculatedate=date.today()
                    score.save()
                    messages.success(request, "Berhasil dihitung.")
        elif('reset' in request.POST):
            errormessage=""
            score = Score.objects.filter(status="DRAFT", changeby=request.user.username).first()
            if (score!=None):
                #Save all attribute
                score.startupname=""
                score.productname=""
                score.sentimentscore=0
                score.infostartupscore=0
                score.infoplatformscore=0
                score.totalscore=0
                score.scorecategory=""
                score.save()
                attributeScores=AttributeScore.objects.filter(score_id=score.id)
                for attributeScore in attributeScores:
                    attributeScore.value=0
                    attributeScore.save()
            if (errormessage!=""):
                messages.error(request, 'Gagal reset. '+errormessage)
            else:
                messages.success(request, 'Berhasil reset.')
        elif('save' in request.POST):
            errormessage=""
            startupname = request.POST['startupname']
            productname = request.POST['productname']
            score = Score.objects.filter(status="DRAFT", changeby=request.user.username).first()
            if (score!=None):
                if (score.calculatedate==None):
                    errormessage="Wajib melakukan Hitung sebelum Simpan."
                    messages.error(request, errormessage)
                #update status to COMPLETE and save
                if (errormessage==""):
                    score.status="COMPLETE"
                    score.changetime=timezone.now()
                    score.save()
                    messages.success(request, "Berhasil disimpan.")
        return redirect('/surpre/score')
    else:
        return redirect('/surpre/score')