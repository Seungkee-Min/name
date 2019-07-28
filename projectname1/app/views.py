from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.generic import ListView, DetailView

#boardList = [{'id': i, 'title': 'title%d' % i, 'content': 'content%d' % i} for i in range(10)]


class IndexView(ListView):
    template_name = 'app/index.html'
    context_object_name = 'boardList'
    def get_queryset(self):
        return Board.objects.all()

# def index(request):
#     # template = loader.get_template('app/index.html')
#     boardList = Board.objects.all()
#     context = {
#         'boardList': boardList
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'app/index.html', context)


class BoardDetail(DetailView):
    template_name = 'app/board.html'
    context_object_name = 'board'
    model = Board
#    def get_queryset(self):
#       return Board.objects.filter(id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = Board.objects.filter(id=self.kwargs.get('pk')).first()
        context['form'] = CommentForm()
        return context


# def detailBoard(request, boardId):
#     #board = Board.objects.filter(id=boardId).first()
#     board = Board.objects.get(id=boardId)
#     '''
#     board = None
#     for b in boardList:
#         if b['id'] == boardId:
#             board = b
#     '''
#     # template = loader.get_template('app/board.html')
#     context = {
#         'board': board
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'app/board.html', context)

def newBoard(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app')
    else:
        form = BoardForm()
        context = {
            'form' : form
        }
        return render(request, 'app/new.html', context)

def BoardDelete(request, boardId):
    board = Board.objects.filter(id=boardId).first()
    board.delete()
    return redirect('/app')

def CommentCreate(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
        return redirect('/app/board/' + str(pk))
