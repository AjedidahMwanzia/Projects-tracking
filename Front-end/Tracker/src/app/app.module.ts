import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule,routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './main/navbar/navbar.component';
import { UserProfileComponent } from './users/user-profile/user-profile.component';
import { UpdateProfileComponent } from './users/update-profile/update-profile.component';
import { LoginComponent } from './users/login/login.component';

import { HomepageComponent } from './homepage/homepage.component';
import { RegisterComponent } from './register/register.component';


@NgModule({
  declarations: [
    AppComponent,

    routingComponents,
    NavbarComponent,
    UserProfileComponent,
    UpdateProfileComponent ,
    HomepageComponent,
    RegisterComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
