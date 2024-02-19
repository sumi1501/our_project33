from django.shortcuts import render
from app.models import *

# Create your views here.
def equijoins(request):
    EQUIJOIN=Emp.objects.select_related('deptno').all()
    EQUIJOIN=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EQUIJOIN=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EQUIJOIN=Emp.objects.select_related('deptno').filter()[:3:]
    EQUIJOIN=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EQUIJOIN=Emp.objects.select_related('deptno').filter(deptno__dname='accounting')
    EQUIJOIN=Emp.objects.select_related('deptno').filter(deptno__dloc='paress')
    EQUIJOIN=Emp.objects.select_related('deptno').filter(deptno=10)
    EQUIJOIN=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EQUIJOIN=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2000)
    EQUIJOIN=Emp.objects.select_related('deptno').all()[1:4:]
    d={'equijoin':EQUIJOIN}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    EMPMGR=Emp.objects.select_related('mgr').all()
    EMPMGR=Emp.objects.select_related('mgr').filter(sal__lt=3000)
    EMPMGR=Emp.objects.select_related('mgr').filter(sal__lte=3000)
    EMPMGR=Emp.objects.select_related('mgr').filter(mgr__job='manager')
    EMPMGR=Emp.objects.select_related('mgr').filter(sal=3000)
    EMPMGR=Emp.objects.select_related('mgr').filter(hiredate__year=2024)
    EMPMGR=Emp.objects.select_related('mgr').filter(ename='king',mgr__deptno=10)
    EMPMGR=Emp.objects.select_related('mgr').filter(comm__isnull=True,mgr__deptno=10)
    EMPMGR=Emp.objects.select_related('mgr').filter(mgr__sal__lt=5000)
    EMPMGR=Emp.objects.select_related('mgr').filter(mgr__hiredate__year=2024)
    EMPMGR=Emp.objects.select_related('mgr').filter(ename__startswith='c')
    EMPMGR=Emp.objects.select_related('mgr').filter(ename__endswith='d')
    EMPMGR=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='b')
    EMPMGR=Emp.objects.select_related('mgr').filter(mgr__sal__lte=1000)
    d={'EMPMGR':EMPMGR}
    return render(request,'selfjoins.html',d)    


def emp_dept_mgr(request):
    emo=Emp.objects.select_related('deptno','mgr').all()
    emo=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=30)
    emo=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year=2024)
    emo=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='sales')
    emo=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='new yourk')
    emo=Emp.objects.select_related('deptno','mgr').filter()[1:4:]
    emo=Emp.objects.select_related('deptno','mgr').filter(ename='blake')
    emo=Emp.objects.select_related('deptno','mgr').filter(job='manager')
    emo=Emp.objects.select_related('deptno','mgr').filter(sal__lt=3000)
    emo=Emp.objects.select_related('deptno','mgr').filter(sal__gt=1000)
    emo=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emo=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emo=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emo=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emo=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emo=Emp.objects.select_related('deptno','mgr').filter(deptno=20)
    emo=Emp.objects.select_related('deptno','mgr').filter(ename='blake',deptno=30)
    emo=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=10)
    d={'emo':emo}
    return render(request,'emp_dept_mgr.html',d)


def emp_salgrade(request):
   SO=Salgrade.objects.filter(grade__in=(1,4))
   EO=Emp.objects.none()
   for sg in SO:
      EO=EO|Emp.objects.filter(sal__range=(sg.losal,sg.maxsal))
   d={'EO':EO,'SO':SO}
   return render(request,'emp_salgrade.html',d)