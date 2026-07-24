# Everything插件Delphi版本搞不定; 把AI搞得心脏病都犯了

### 来源信息
- **URL**: https://www.52pojie.cn/thread-2119135-1-1.html
- **来源站点**: 吾爱破解
- **页面抓取**: 成功

### 页面正文
| 本帖最后由 冥界3大法王 于 2026-7-24 14:43 编辑 
 
 [Delphi] 纯文本查看 复制代码 library EverythingGrokPlugin;
uses
  Winapi.Windows,
  Winapi.Messages,  // WM_SETTEXT 需要
  System.SysUtils,
  System.Classes,
  Vcl.Forms,
  Vcl.Dialogs,  // mrOK 需要
  System.UITypes,
  MainForm in 'MainForm.pas';
type
  TPluginInfo = record
  Version: Integer;
  Flags: Integer;
  Name: PChar;
  Description: PChar;
  end;
function GetPluginInfo: TPluginInfo; stdcall;
begin
  Result.Version := 1;
  Result.Flags := 0;
  Result.Name := 'Grok 高级搜索';
  Result.Description := '加载即弹出';
end;
procedure SendQueryToEverything(const Query: string);
var
  H, E: HWND;
begin
  H := FindWindow('EVERYTHING_(1.5a)', nil);
  if H = 0 then Exit;
  E := FindWindowEx(H, 0, 'Edit', nil);
  if E <> 0 then
  begin
  SendMessage(E, WM_SETTEXT, 0, LPARAM(PChar(Query)));
  SetForegroundWindow(H);
  end;
end;
procedure ExecuteSearch;
var
  Form: TfrmEverythingHelper;
  Query: string;
begin
  Form := TfrmEverythingHelper.Create(nil);
  try
  if Form.ShowModal = mrOK then
  begin
  Query := Trim(Form.Memo1.Text);
  if Query <> '' then
  SendQueryToEverything(Query);
  end;
  finally
  Form.Free;
  end;
end;
procedure OnToolbarButtonClick; stdcall;
begin
  ExecuteSearch;
end;
procedure ExecuteCommand(const Params: PChar); stdcall;
begin
  ExecuteSearch;
end;
exports
  GetPluginInfo,
  OnToolbarButtonClick,
  ExecuteCommand;
begin
  // DLL 加载成功后立即弹出界面
  ExecuteSearch;
end.
 
 
 
 [Delphi] 纯文本查看 复制代码 unit MainForm;
interface
uses
  Clipbrd, Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs,
  Vcl.StdCtrls, Vcl.ExtCtrls, Vcl.Buttons;
type
  TfrmEverythingHelper = class(TForm)
  Panel1: TPanel;
  Label1: TLabel;
  ComboBox1: TComboBox; // 搜索类型
  Edit1: TEdit;  // 搜索内容
  Label2: TLabel;
  ComboBox2: TComboBox; // 修饰符
  btnGenerate: TButton;
  btnCopy: TButton;
  btnSendToEverything: TButton;
  Memo1: TMemo;  // 查询预览
  procedure FormCreate(Sender: TObject);
  procedure btnGenerateClick(Sender: TObject);
  procedure btnCopyClick(Sender: TObject);
  procedure btnSendToEverythingClick(Sender: TObject);
  private
  function BuildQuery: string;
  function FindEverythingEdit(out AMainHWnd: HWND): HWND;
  procedure SendToEverything(const Query: string);
  public
  { Public declarations }
  end;
var
  frmEverythingHelper: TfrmEverythingHelper;
implementation
procedure TfrmEverythingHelper.FormCreate(Sender: TObject);
begin
  Caption := 'Everything 高级查询助手';
  Position := poScreenCenter;
  BorderStyle := bsDialog;
  // 初始化 ComboBox1 - 常用搜索类型
  ComboBox1.Items.Clear;
  ComboBox1.Items.Add('content:'); // 内容搜索
  ComboBox1.Items.Add('name:');  // 文件名
  ComboBox1.Items.Add('path:');  // 路径
  ComboBox1.Items.Add('ext:');  // 扩展名
  ComboBox1.Items.Add('size:');  // 大小
  ComboBox1.Items.Add('dm:');  // 修改日期
  ComboBox1.ItemIndex := 0;
  // 初始化 ComboBox2 - 常用修饰符
  ComboBox2.Items.Clear;
  ComboBox2.Items.Add('');  // 无
  ComboBox2.Items.Add('regex:');
  ComboBox2.Items.Add('case:');
  ComboBox2.Items.Add('whole:');
  ComboBox2.Items.Add('ww:');  // whole word
  ComboBox2.ItemIndex := 0;
  Memo1.Clear;
  Memo1.ReadOnly := False; // 允许用户手动微调生成的语句
end;
function TfrmEverythingHelper.BuildQuery: string;
var
  Base, Content, Modifier: string;
begin
  Base := Trim(ComboBox1.Text);
  Content := Trim(Edit1.Text);
  Modifier := Trim(ComboBox2.Text);
  if Content = '' then
  Result := ''
  else
  begin
  if Modifier <> '' then
  Result := Modifier + Base + Content
  else
  Result := Base + Content;
  end;
end;
// 动态查找 Everything 的 Edit 控件及主窗口句柄
function TfrmEverythingHelper.FindEverythingEdit(out AMainHWnd: HWND): HWND;
var
  hMain, hToolbar, hEdit: HWND;
begin
  Result := 0;
  AMainHWnd := 0;
  // 1. 尝试查找 1.5a Alpha 版主窗口
  hMain := FindWindow('EVERYTHING_(1.5a)', nil);
  // 2. 若未查到，尝试查找 1.x 标准版主窗口
  if hMain = 0 then
  hMain := FindWindow('EVERYTHING', nil);
  if hMain = 0 then Exit;
  AMainHWnd := hMain;
  // 3. 优先寻找工具栏内的 Edit 控件 (常规 1.5a 结构)
  hToolbar := FindWindowEx(hMain, 0, 'EVERYTHING_TOOLBAR', nil);
  if hToolbar <> 0 then
  begin
  hEdit := FindWindowEx(hToolbar, 0, 'Edit', nil);
  if hEdit <> 0 then
  begin
  Result := hEdit;
  Exit;
  end;
  end;
  // 4. 若未在工具栏内找到，尝试直接寻找主窗口下的 Edit 控件
  hEdit := FindWindowEx(hMain, 0, 'Edit', nil);
  Result := hEdit;
end;
procedure TfrmEverythingHelper.btnGenerateClick(Sender: TObject);
begin
  Memo1.Text := BuildQuery;
end;
procedure TfrmEverythingHelper.btnCopyClick(Sender: TObject);
var
  S: string;
begin
  S := Trim(Memo1.Text);
  if S = '' then
  S := BuildQuery;
  if S <> '' then
  begin
  Clipboard.AsText := S;
  ShowMessage('已复制到剪贴板：' + sLineBreak + S);
  end
  else
  ShowMessage('请输入搜索内容！');
end;
procedure TfrmEverythingHelper.SendToEverything(const Query: string);
var
  hMainHWnd, hEditHWnd: HWND;
begin
  hEditHWnd := FindEverythingEdit(hMainHWnd);
  if hMainHWnd = 0 then
  begin
  ShowMessage('未找到 Everything 运行实例，请先启动 Everything！');
  Exit;
  end;
  if hEditHWnd <> 0 then
  begin
  // 设置搜索文本
  SendMessage(hEditHWnd, WM_SETTEXT, 0, LPARAM(PChar(Query)));
  // 激活并前置 Everything 主窗口
  if IsIconic(hMainHWnd) then
  ShowWindow(hMainHWnd, SW_RESTORE);
  SetForegroundWindow(hMainHWnd);
  end
  else
  begin
  ShowMessage('未能找到 Everything 搜索框控件！');
  end;
end;
procedure TfrmEverythingHelper.btnSendToEverythingClick(Sender: TObject);
var
  S: string;
begin
  // 优先使用 Memo1 中的文本（支持用户手动修改后的内容）
  S := Trim(Memo1.Text);
  if S = '' then
  begin
  S := BuildQuery;
  Memo1.Text := S;
  end;
  if S <> '' then
  SendToEverything(S)
  else
  ShowMessage('请输入搜索内容！');
end;
end.
 
 
 
 插件正常加载了，但是 窗口出来阻塞 了 后台无法切换Everything 's Edit 控件了。。。
 后来又换了模态的窗口。。。
 直接导致程序崩溃。。。改了又是很多次 。。。就连AI也搞不定
 
 后来想到可以用C++的DLL调用Delphi的DLL或许有戏
 或者干脆使用C++ builder来写
 |

---
*爬取时间: 2026-07-24 21:59:19*
*来源: 直接站点爬取*
