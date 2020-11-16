import { Component, EventEmitter, NgZone, ViewChild } from "@angular/core";
import * as _ from "lodash";
import { DatabaseService, ChatMessage, UtilService } from '../providers';

@Component({
  selector: 'page-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss']
})

export class HomePage {
  @ViewChild('txtChat') txtChat: any;
  @ViewChild('content') content: any;
  messages: any[];
  chatBox: string;
  btnEmitter: EventEmitter<string>;

  constructor(public _zone: NgZone,
    public databaseService: DatabaseService) {
    this.btnEmitter = new EventEmitter<string>();
    this.messages = [
      { type: 'message_request', from: 'Aliasgher', message: "Hello World1", epoch: "432423424" },
      { type: 'message_response', from: 'Hamza', message: "Hello World2", epoch: 4324234234 },
      { type: 'message_request', from: 'Aliasgher', message: "Hello World3", epoch: 4324234234 },
      { type: 'message_response', from: 'Hamza', message: "Hello World4", epoch: 4324234234 },
    ];
    this.chatBox = "";
    this.init();
  }

  ionViewWillEnter() {
    this.databaseService.getJson("messages")
      .then(messages => {
        if (messages) {
          this.messages = this.messages.concat(_.sortBy(messages, ['epoch']));
        }
        this.scrollToBottom();
      });
  }

  ionViewWillLeave() {

  }

  init() {
    // this.socketService.messages.subscribe((chatMessage: ChatMessage) => {
    //   this._zone.run(() => {
    //     this.messages.push(chatMessage);
    //   });
    //   this.scrollToBottom();
    // });
  }

  public sendMessage() {
    this.btnEmitter.emit("sent clicked");
    this.txtChat.setFocus();
    let message = this.txtChat.content;
    this.send(message);
    this.txtChat.clearInput();
  }

  send(message) {
    //todo read email from database
    let from = "annaggarwal@paypal.com";
    // this.socketService.newRequest(UtilService.formatMessageRequest(message, from));
    this.chatBox = '';
    this.scrollToBottom();
  }

  scrollToBottom() {
    this._zone.run(() => {
      setTimeout(() => {
        this.content.scrollToBottom(300);
      });
    });
  }
}
