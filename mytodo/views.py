from django.shortcuts import render, redirect
from django.views import View # クラスベースビューを継承するのに必要
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskForm

class IndexView(View):
    def get(self, request):
        # todoリストを取得
        todo_list = Task.objects.order_by('complete')
        context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)


class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):


        form = TaskForm(request.POST)

        is_valid = form.is_valid()


        if is_valid:

            form.save()
            return redirect('/')

        return render(request, 'mytodo/add.html', {'form': form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')
    
class TaskUpdateView(UpdateView):
    model = Task                     
    form_class = TaskForm
    template_name = 'mytodo/add.html'
    success_url = '/'               

class Task_delete(View):
    def get(self, request, pk, *args, **kwargs):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance = task)
        
        for field in form.fields.values():
            field.disabled = True
        return render(request, "mytodo/delete.html", {'form': form, 'task_id':pk})

    def post(self, request, pk, *args, **kwargs):
        Task.objects.filter(id=pk).delete()
        return redirect('/')

index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = Update_task_complete.as_view()
task_delete = Task_delete.as_view()