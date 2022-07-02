import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './users/login/login.component';
import { UserProfileComponent } from './users/user-profile/user-profile.component';

const routes: Routes = [
  {path:'login', component:LoginComponent},
  {path:'my-profile',component:UserProfileComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
// array of all routing components
export const routingComponents = [LoginComponent]